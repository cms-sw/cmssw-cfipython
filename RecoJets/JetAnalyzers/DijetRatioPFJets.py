import FWCore.ParameterSet.Config as cms

def DijetRatioPFJets(**kwargs):
  mod = cms.EDAnalyzer('DijetRatioPFJets',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
