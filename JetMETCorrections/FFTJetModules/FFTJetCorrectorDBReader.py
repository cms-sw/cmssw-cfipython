import FWCore.ParameterSet.Config as cms

def FFTJetCorrectorDBReader(**kwargs):
  mod = cms.EDAnalyzer('FFTJetCorrectorDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
