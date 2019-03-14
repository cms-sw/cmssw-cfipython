import FWCore.ParameterSet.Config as cms

hltPFJetIDProducer = cms.EDProducer('HLTPFJetIDProducer',
  minPt = cms.double(20),
  maxEta = cms.double(1e+99),
  CHF = cms.double(-99),
  NHF = cms.double(99),
  CEF = cms.double(99),
  NEF = cms.double(99),
  maxCF = cms.double(99),
  NCH = cms.int32(0),
  NTOT = cms.int32(0),
  jetsInput = cms.InputTag('hltAntiKT4PFJets')
)
