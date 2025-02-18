import FWCore.ParameterSet.Config as cms

def HLTEcalUncalibratedRecHitInAllL1RegionsProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTEcalUncalibratedRecHitInAllL1RegionsProducer',
    productLabels = cms.vstring(
      'EcalRegionalRecHitsEB',
      'EcalRegionalRecHitsEE'
    ),
    recHitLabels = cms.VInputTag(
      'hltEcalRegionalEgammaRecHit:EcalRecHitsEB',
      'hltEcalRegionalEgammaRecHit:EcalRecHitsEE',
      'hltESRegionalEgammaRecHit:EcalRecHitsES'
    ),
    l1InputRegions = cms.VPSet(
      cms.PSet(
        inputColl = cms.InputTag('hltL1extraParticles', 'NonIsolated'),
        maxEt = cms.double(999),
        minEt = cms.double(5),
        regionEtaMargin = cms.double(0.14),
        regionPhiMargin = cms.double(0.4),
        type = cms.string('L1EmParticle')
      ),
      cms.PSet(
        inputColl = cms.InputTag('hltL1extraParticles', 'Isolated'),
        maxEt = cms.double(999),
        minEt = cms.double(5),
        regionEtaMargin = cms.double(0.14),
        regionPhiMargin = cms.double(0.4),
        type = cms.string('L1EmParticle')
      ),
      cms.PSet(
        inputColl = cms.InputTag('hltCaloStage2Digis'),
        maxEt = cms.double(999),
        minEt = cms.double(5),
        regionEtaMargin = cms.double(0.4),
        regionPhiMargin = cms.double(0.5),
        type = cms.string('EGamma')
      ),
      cms.PSet(
        inputColl = cms.InputTag('hltCaloStage2Digis'),
        maxEt = cms.double(999),
        minEt = cms.double(200),
        regionEtaMargin = cms.double(0.4),
        regionPhiMargin = cms.double(0.5),
        type = cms.string('EGamma')
      ),
      template = cms.PSetTemplate(
        type = cms.required.string,
        minEt = cms.required.double,
        maxEt = cms.required.double,
        regionEtaMargin = cms.required.double,
        regionPhiMargin = cms.required.double,
        inputColl = cms.required.InputTag
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
