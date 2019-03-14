import FWCore.ParameterSet.Config as cms

hiFJRhoProducer = cms.EDProducer('HiFJRhoProducer',
  jetSource = cms.InputTag('kt4PFJets'),
  nExcl = cms.int32(2),
  etaMaxExcl = cms.double(2),
  ptMinExcl = cms.double(20),
  nExcl2 = cms.int32(2),
  etaMaxExcl2 = cms.double(2),
  ptMinExcl2 = cms.double(20)
)
