import FWCore.ParameterSet.Config as cms

def SiPixelQualityProbabilitiesWriteFromASCII(**kwargs):
  mod = cms.EDAnalyzer('SiPixelQualityProbabilitiesWriteFromASCII',
    printDebug = cms.untracked.bool(True),
    record = cms.string('SiPixelStatusScenarioProbabilityRcd'),
    probabilities = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
