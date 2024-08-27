import FWCore.ParameterSet.Config as cms

def DijetMassGenJets(**kwargs):
  mod = cms.EDAnalyzer('DijetMassGenJets',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
