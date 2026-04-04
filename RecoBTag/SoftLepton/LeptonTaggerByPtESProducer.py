import FWCore.ParameterSet.Config as cms

def LeptonTaggerByPtESProducer(*args, **kwargs):
  mod = cms.ESProducer('LeptonTaggerByPtESProducer',
    ipSign = cms.string('any'),
    leptonId = cms.string(''),
    qualityCut = cms.double(0.5),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
