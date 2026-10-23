import FWCore.ParameterSet.Config as cms

def EcalPulseShapeGrapher(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalPulseShapeGrapher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
