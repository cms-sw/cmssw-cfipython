import FWCore.ParameterSet.Config as cms

globalReco = cms.EDProducer('MtdGlobalRecoValidation',
  folder = cms.string('MTD/GlobalReco'),
  inputTagT = cms.InputTag('trackExtenderWithMTD'),
  inputTagV = cms.InputTag('offlinePrimaryVertices4D'),
  trackMinimumEnergy = cms.double(1),
  trackMinimumEta = cms.double(1.5),
  trackMaximumEta = cms.double(3.2),
  mightGet = cms.optional.untracked.vstring
)
