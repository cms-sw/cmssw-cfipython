import FWCore.ParameterSet.Config as cms

def TrackerOfflineValidation(**kwargs):
  mod = cms.EDAnalyzer('TrackerOfflineValidation',
    trajectoryInput = cms.string('generalTracks'),
    Tracks = cms.InputTag('generalTracks'),
    compressionSettings = cms.untracked.int32(-1),
    localCoorHistosOn = cms.bool(False),
    moduleLevelHistsTransient = cms.bool(False),
    moduleLevelProfiles = cms.bool(False),
    stripYResiduals = cms.bool(False),
    useFwhm = cms.bool(True),
    useFit = cms.bool(False),
    useOverflowForRMS = cms.bool(False),
    useInDqmMode = cms.bool(False),
    moduleDirectoryInOutput = cms.string(''),
    chargeCut = cms.int32(0),
    maxTracks = cms.uint64(0),
    TH1XResPixelModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1XResStripModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1NormXResPixelModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1NormXResStripModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1XprimeResPixelModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1XprimeResStripModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1NormXprimeResPixelModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1NormXprimeResStripModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1YResPixelModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1YResStripModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1NormYResPixelModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1NormYResStripModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TProfileXResPixelModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TProfileXResStripModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TProfileYResPixelModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TProfileYResStripModules = cms.PSet(
      Nbinx = cms.int32(100),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
