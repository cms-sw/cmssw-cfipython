import FWCore.ParameterSet.Config as cms

def MPISenderPortable_alpaka(*args, **kwargs):
  mod = cms.EDProducer('MPISenderPortable@alpaka',
    upstream = cms.InputTag('source'),
    products = cms.VPSet(
      template = cms.PSetTemplate(
        type = cms.required.string,
        src = cms.required.InputTag
      )
    ),
    instance = cms.int32(0),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
