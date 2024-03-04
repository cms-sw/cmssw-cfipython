import FWCore.ParameterSet.Config as cms

def ValidationHcalIsoTrackAlCaReco(**kwargs):
  mod = cms.EDAnalyzer('ValidationHcalIsoTrackAlCaReco',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
