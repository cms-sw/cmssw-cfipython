import FWCore.ParameterSet.Config as cms

L2TauJetsMerger = cms.EDProducer('L2TauJetsMerger',
  JetSrc = cms.VInputTag(
    'hltAkIsoTau1Regional',
    'hltAkIsoTau2Regional',
    'hltAkIsoTau3Regional',
    'hltAkIsoTau4Regional'
  ),
  EtMin = cms.double(20)
)
