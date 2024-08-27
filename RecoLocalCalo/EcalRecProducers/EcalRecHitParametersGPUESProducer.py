import FWCore.ParameterSet.Config as cms

def EcalRecHitParametersGPUESProducer(**kwargs):
  mod = cms.ESSource('EcalRecHitParametersGPUESProducer',
    ChannelStatusToBeExcluded = cms.vstring(
      'kDAC',
      'kNoisy',
      'kNNoisy',
      'kFixedG6',
      'kFixedG1',
      'kFixedG0',
      'kNonRespondingIsolated',
      'kDeadVFE',
      'kDeadFE',
      'kNoDataNoTP'
    ),
    flagsMapDBReco = cms.PSet(
      kGood = cms.vstring(
        'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy'
      ),
      kNoisy = cms.vstring(
        'kNNoisy',
        'kFixedG6',
        'kFixedG1'
      ),
      kNeighboursRecovered = cms.vstring(
        'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE'
      ),
      kTowerRecovered = cms.vstring('kDeadFE'),
      kDead = cms.vstring('kNoDataNoTP')
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
