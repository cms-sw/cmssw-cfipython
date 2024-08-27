import FWCore.ParameterSet.Config as cms

def PATPuppiJetSpecificProducer(**kwargs):
  mod = cms.EDProducer('PATPuppiJetSpecificProducer',
    src = cms.InputTag('slimmedJets'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
