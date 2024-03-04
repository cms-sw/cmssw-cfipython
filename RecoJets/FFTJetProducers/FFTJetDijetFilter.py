import FWCore.ParameterSet.Config as cms

def FFTJetDijetFilter(**kwargs):
  mod = cms.EDFilter('FFTJetDijetFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
