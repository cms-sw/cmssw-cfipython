import FWCore.ParameterSet.Config as cms

def CITKPFIsolationSumProducer(**kwargs):
  mod = cms.EDProducer('CITKPFIsolationSumProducer',
    srcToIsolate = cms.InputTag('no default'),
    srcForIsolationCone = cms.InputTag('no default'),
    isolationConeDefinitions = cms.VPSet(
      cms.PSet(),
      cms.PSet(),
      cms.PSet()
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
