import FWCore.ParameterSet.Config as cms

def LumiProducerFromBrilcalc(**kwargs):
  mod = cms.EDProducer('LumiProducerFromBrilcalc',
    lumiFile = cms.required.string,
    throwIfNotFound = cms.bool(False),
    doBunchByBunch = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
