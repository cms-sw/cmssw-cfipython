import FWCore.ParameterSet.Config as cms

def TauJetCorrectorExample(**kwargs):
  mod = cms.EDAnalyzer('TauJetCorrectorExample',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
