import FWCore.ParameterSet.Config as cms

fixedGridRhoProducerFastjetFromRecHit = cms.EDProducer('FixedGridRhoProducerFastjetFromRecHit',
  hbheRecHitsTag = cms.InputTag('hltHbhereco'),
  ebRecHitsTag = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEB'),
  eeRecHitsTag = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEE'),
  skipHCAL = cms.bool(False),
  skipECAL = cms.bool(False),
  eThresHB = cms.vdouble(
    0.1,
    0.2,
    0.3,
    0.3
  ),
  eThresHE = cms.vdouble(
    0.1,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2
  ),
  maxRapidity = cms.double(2.5),
  gridSpacing = cms.double(0.55),
  mightGet = cms.optional.untracked.vstring
)
