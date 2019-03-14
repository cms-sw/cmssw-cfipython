import FWCore.ParameterSet.Config as cms

PUFilter = cms.EDProducer('PUFilter',
  Jets = cms.InputTag('hltAK4PFJetsCorrected'),
  JetPUID = cms.InputTag('MVAJetPuIdProducer', 'CATEv0Id')
)
