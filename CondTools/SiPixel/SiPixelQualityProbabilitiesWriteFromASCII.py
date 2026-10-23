import FWCore.ParameterSet.Config as cms

def SiPixelQualityProbabilitiesWriteFromASCII(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelQualityProbabilitiesWriteFromASCII',
    printDebug = cms.untracked.bool(True),
    record = cms.string('SiPixelStatusScenarioProbabilityRcd'),
    probabilities = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
