import FWCore.ParameterSet.Config as cms

def TtSemiLepKinFitProducerElectron(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepKinFitProducerElectron',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
