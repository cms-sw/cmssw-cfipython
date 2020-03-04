import FWCore.ParameterSet.Config as cms

etlReco = cms.EDProducer('EtlRecoValidation',
  folder = cms.string('MTD/ETL/Reco'),
  inputTagC = cms.InputTag('mtdClusters', 'FTLEndcap'),
  inputTagT = cms.InputTag('trackExtenderWithMTD'),
  hitMinimumEnergy = cms.double(1),
  trackMinimumEnergy = cms.double(0.5),
  trackMinimumEta = cms.double(1.4),
  trackMaximumEta = cms.double(3.2),
  mightGet = cms.optional.untracked.vstring
)
