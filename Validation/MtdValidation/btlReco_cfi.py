import FWCore.ParameterSet.Config as cms

btlReco = cms.EDProducer('BtlRecoValidation',
  folder = cms.string('MTD/BTL/Reco'),
  inputTagC = cms.InputTag('mtdClusters', 'FTLBarrel'),
  inputTagT = cms.InputTag('trackExtenderWithMTD'),
  inputTagV = cms.InputTag('offlinePrimaryVertices4D'),
  hitMinimumEnergy = cms.double(1),
  trackMinimumEnergy = cms.double(1),
  trackMinimumEta = cms.double(1.5),
  mightGet = cms.optional.untracked.vstring
)
