import FWCore.ParameterSet.Config as cms

def METTester(*args, **kwargs):
  mod = cms.EDProducer('METTester',
    runDir = cms.untracked.string('JetMET/METValidation/'),
    primaryVertices = cms.InputTag('PixelVertices'),
    inputMETLabel = cms.InputTag('pfMet'),
    METType = cms.untracked.string('pf'),
    genMetTrue = cms.InputTag('genMetTrue'),
    genMetCalo = cms.InputTag('genMetCalo'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
