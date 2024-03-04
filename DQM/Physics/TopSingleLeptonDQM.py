import FWCore.ParameterSet.Config as cms

def TopSingleLeptonDQM(**kwargs):
  mod = cms.EDProducer('TopSingleLeptonDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
