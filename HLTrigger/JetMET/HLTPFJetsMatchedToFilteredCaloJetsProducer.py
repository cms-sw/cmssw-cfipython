import FWCore.ParameterSet.Config as cms

def HLTPFJetsMatchedToFilteredCaloJetsProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTPFJetsMatchedToFilteredCaloJetsProducer',
    src = cms.InputTag('hltJets'),
    triggerJetsFilter = cms.InputTag('hltCaloJetsFiltered'),
    triggerJetsType = cms.int32(85),
    maxDeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
