import FWCore.ParameterSet.Config as cms

def HiSignalGenJetProducer(*args, **kwargs):
  mod = cms.EDProducer('HiSignalGenJetProducer',
    src = cms.InputTag('akHiGenJets'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
