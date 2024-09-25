import FWCore.ParameterSet.Config as cms

def SiPixelPhase1Analyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelPhase1Analyzer',
    src = cms.InputTag('generalTracks'),
    opMode = cms.untracked.uint32(1),
    debugFileName = cms.untracked.string('debug.txt'),
    isBarrelSource = cms.untracked.vuint32(
      0,
      0,
      1
    ),
    remapRootFileName = cms.untracked.vstring('dqmFile.root'),
    pathToHistograms = cms.untracked.vstring(
      'DQMData/Run 1/PixelPhase1/Run summary/Phase1_MechanicalView/PXForward/',
      'DQMData/Run 1/PixelPhase1/Run summary/Phase1_MechanicalView/PXForward/',
      'DQMData/Run 1/PixelPhase1/Run summary/Phase1_MechanicalView/PXBarrel/'
    ),
    baseHistogramName = cms.untracked.vstring(
      'num_clusters_per_PXDisk_per_SignedBladePanel_PXRing',
      'num_digis_per_PXDisk_per_SignedBladePanel_PXRing',
      'num_digis_per_SignedModule_per_SignedLadder_PXLayer'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
