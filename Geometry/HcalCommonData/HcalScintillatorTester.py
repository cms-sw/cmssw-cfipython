import FWCore.ParameterSet.Config as cms

def HcalScintillatorTester(**kwargs):
  mod = cms.EDAnalyzer('HcalScintillatorTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
