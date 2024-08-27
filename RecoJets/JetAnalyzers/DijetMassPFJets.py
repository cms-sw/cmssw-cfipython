import FWCore.ParameterSet.Config as cms

def DijetMassPFJets(**kwargs):
  mod = cms.EDAnalyzer('DijetMassPFJets',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
