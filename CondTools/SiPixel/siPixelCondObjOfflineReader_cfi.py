import FWCore.ParameterSet.Config as cms

siPixelCondObjOfflineReader = cms.EDAnalyzer('SiPixelCondObjOfflineReader',
  useSimRcd = cms.bool(False),
  maxRangeDeadPixHist = cms.untracked.double(0.001),
  mightGet = cms.optional.untracked.vstring
)
