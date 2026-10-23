import FWCore.ParameterSet.Config as cms

def SiPixelQualityProbabilitiesTestWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelQualityProbabilitiesTestWriter',
    printDebug = cms.untracked.bool(True),
    record = cms.string('SiPixelStatusScenarioProbabilityRcd'),
    snapshots = cms.string(''),
    probabilities = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
