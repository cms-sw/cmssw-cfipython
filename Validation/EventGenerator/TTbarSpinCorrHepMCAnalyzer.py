import FWCore.ParameterSet.Config as cms

def TTbarSpinCorrHepMCAnalyzer(**kwargs):
  mod = cms.EDProducer('TTbarSpinCorrHepMCAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
