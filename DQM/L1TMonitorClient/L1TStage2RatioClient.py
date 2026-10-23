import FWCore.ParameterSet.Config as cms

def L1TStage2RatioClient(*args, **kwargs):
  mod = cms.EDProducer('L1TStage2RatioClient',
    monitorDir = cms.untracked.string(''),
    inputNum = cms.untracked.string(''),
    inputDen = cms.untracked.string(''),
    ratioName = cms.untracked.string('ratio'),
    ratioTitle = cms.untracked.string('ratio'),
    yAxisTitle = cms.untracked.string(''),
    binomialErr = cms.untracked.bool(True),
    ignoreBin = cms.untracked.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
