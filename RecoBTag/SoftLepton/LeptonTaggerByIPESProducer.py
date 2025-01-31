import FWCore.ParameterSet.Config as cms

def LeptonTaggerByIPESProducer(*args, **kwargs):
  mod = cms.ESProducer('LeptonTaggerByIPESProducer',
    ipSign = cms.string('any'),
    leptonId = cms.string(''),
    qualityCut = cms.double(0.5),
    use3d = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
