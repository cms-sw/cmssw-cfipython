import FWCore.ParameterSet.Config as cms

dqmCorrelationClient = cms.EDProducer('DQMCorrelationClient',
  me1onX = cms.bool(True),
  me = cms.PSet(
    doXaxis = cms.bool(True),
    nbinsX = cms.int32(2500),
    xminX = cms.double(0),
    xmaxX = cms.double(2500),
    doYaxis = cms.bool(True),
    nbinsY = cms.int32(2500),
    xminY = cms.double(0),
    xmaxY = cms.double(2500)
  ),
  me1 = cms.PSet(
    folder = cms.string(''),
    name = cms.string(''),
    profileX = cms.bool(True)
  ),
  me2 = cms.PSet(
    folder = cms.string(''),
    name = cms.string(''),
    profileX = cms.bool(True)
  )
)
