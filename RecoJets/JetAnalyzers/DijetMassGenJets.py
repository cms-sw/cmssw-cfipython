import FWCore.ParameterSet.Config as cms

def DijetMassGenJets(*args, **kwargs):
  mod = cms.EDAnalyzer('DijetMassGenJets',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
