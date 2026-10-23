import FWCore.ParameterSet.Config as cms

def LumiProducerFromBrilcalc(*args, **kwargs):
  mod = cms.EDProducer('LumiProducerFromBrilcalc',
    lumiFile = cms.required.string,
    throwIfNotFound = cms.bool(False),
    doBunchByBunch = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
