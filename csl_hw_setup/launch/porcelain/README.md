# Porcelain directory documentation

Wed Oct 26 08:49:40 EEST 2016, Nikos Koukis

Porcelain directory launchfiles (as in git-porcelain commands) are to be
launched *directly* by the User to setup/execute single/multi-robot SLAM. To do that, they
utilize plumbing launchfiles found in the `plumbing/` directory.

Typical operations of files stored in this directory include:

- Single/multi-robot graphSLAM either in an online setup or from a
    rosbag
- Ground-Truth data acquisition
