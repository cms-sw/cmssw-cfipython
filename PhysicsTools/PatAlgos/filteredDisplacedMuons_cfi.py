import FWCore.ParameterSet.Config as cms

filteredDisplacedMuons = cms.EDProducer('DisplacedMuonFilterProducer',
  srcMuons = cms.InputTag('displacedMuons'),
  FillTimingInfo = cms.bool(True),
  FillDetectorBasedIsolation = cms.bool(False),
  TrackIsoDeposits = cms.InputTag('displacedMuons', 'tracker'),
  JetIsoDeposits = cms.InputTag('displacedMuons', 'jets'),
  EcalIsoDeposits = cms.InputTag('displacedMuons', 'ecal'),
  HcalIsoDeposits = cms.InputTag('displacedMuons', 'hcal'),
  HoIsoDeposits = cms.InputTag('displacedMuons', 'ho'),
  minPtSTA = cms.double(3.5),
  minPtTK = cms.double(3.5),
  minMatches = cms.double(2),
  mightGet = cms.optional.untracked.vstring
)
