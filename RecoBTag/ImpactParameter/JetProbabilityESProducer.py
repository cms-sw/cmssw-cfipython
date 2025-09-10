import FWCore.ParameterSet.Config as cms

def JetProbabilityESProducer(*args, **kwargs):
  mod = cms.ESProducer('JetProbabilityESProducer',
    impactParameterType = cms.int32(0),
    minimumProbability = cms.double(0.005),
    deltaR = cms.double(0.3),
    trackIpSign = cms.int32(1),
    maximumDecayLength = cms.double(5),
    maximumDistanceToJetAxis = cms.double(0.07),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False),
    a_dR = cms.double(-0.001053),
    b_dR = cms.double(0.6263),
    a_pT = cms.double(0.005263),
    b_pT = cms.double(0.3684),
    min_pT = cms.double(120),
    max_pT = cms.double(500),
    min_pT_dRcut = cms.double(0.5),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
