import FWCore.ParameterSet.Config as cms

def EcalPulseShapeGrapher(**kwargs):
  mod = cms.EDAnalyzer('EcalPulseShapeGrapher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
