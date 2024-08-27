import FWCore.ParameterSet.Config as cms

def HLTPFJetsMatchedToFilteredPFJetsProducer(**kwargs):
  mod = cms.EDProducer('HLTPFJetsMatchedToFilteredPFJetsProducer',
    src = cms.InputTag('hltJets'),
    triggerJetsFilter = cms.InputTag('hltCaloJetsFiltered'),
    triggerJetsType = cms.int32(85),
    maxDeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
