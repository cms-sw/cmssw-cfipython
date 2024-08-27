import FWCore.ParameterSet.Config as cms

def SiPixelQualityProbabilitiesTestWriter(**kwargs):
  mod = cms.EDAnalyzer('SiPixelQualityProbabilitiesTestWriter',
    printDebug = cms.untracked.bool(True),
    record = cms.string('SiPixelStatusScenarioProbabilityRcd'),
    snapshots = cms.string(''),
    probabilities = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
