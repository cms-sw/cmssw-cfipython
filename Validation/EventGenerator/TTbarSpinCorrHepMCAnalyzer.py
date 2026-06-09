import FWCore.ParameterSet.Config as cms

def TTbarSpinCorrHepMCAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('TTbarSpinCorrHepMCAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
