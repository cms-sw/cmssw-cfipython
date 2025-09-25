import FWCore.ParameterSet.Config as cms

def EcalSeverityLevelESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalSeverityLevelESProducer',
    flagMask = cms.PSet(
      kGood = cms.vstring('kGood'),
      kProblematic = cms.vstring(
        'kPoorReco',
        'kPoorCalib',
        'kNoisy',
        'kSaturated'
      ),
      kRecovered = cms.vstring(
        'kLeadingEdgeRecovered',
        'kTowerRecovered'
      ),
      kTime = cms.vstring('kOutOfTime'),
      kWeird = cms.vstring(
        'kWeird',
        'kDiWeird'
      ),
      kBad = cms.vstring(
        'kFaultyHardware',
        'kDead',
        'kKilled'
      )
    ),
    dbstatusMask = cms.PSet(
      kGood = cms.vstring('kOk'),
      kProblematic = cms.vstring(
        'kDAC',
        'kNoLaser',
        'kNoisy',
        'kNNoisy',
        'kNNNoisy',
        'kNNNNoisy',
        'kNNNNNoisy',
        'kFixedG6',
        'kFixedG1',
        'kFixedG0'
      ),
      kRecovered = cms.vstring(),
      kTime = cms.vstring(),
      kWeird = cms.vstring(),
      kBad = cms.vstring(
        'kNonRespondingIsolated',
        'kDeadVFE',
        'kDeadFE',
        'kNoDataNoTP'
      )
    ),
    timeThresh = cms.double(2),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
