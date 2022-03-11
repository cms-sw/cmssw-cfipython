import FWCore.ParameterSet.Config as cms

pfType1MET = cms.EDProducer('Type1PFMET',
  inputUncorJetsTag = cms.InputTag('ak4PFJets'),
  jetEMfracLimit = cms.double(0.95),
  jetMufracLimit = cms.double(0.95),
  metType = cms.string('PFMET'),
  jetPTthreshold = cms.double(20),
  inputUncorMetLabel = cms.InputTag('pfMET'),
  corrector = cms.InputTag('ak4PFL2L3Corrector'),
  mightGet = cms.optional.untracked.vstring
)
