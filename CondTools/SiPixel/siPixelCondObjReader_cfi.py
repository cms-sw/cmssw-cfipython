import FWCore.ParameterSet.Config as cms

siPixelCondObjReader = cms.EDAnalyzer('SiPixelCondObjReader',
  maxRangeDeadPixHist = cms.untracked.double(0.001),
  mightGet = cms.optional.untracked.vstring
)
