import FWCore.ParameterSet.Config as cms

def PATPuppiJetSpecificProducer(*args, **kwargs):
  mod = cms.EDProducer('PATPuppiJetSpecificProducer',
    src = cms.InputTag('slimmedJets'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
