import FWCore.ParameterSet.Config as cms

def HLTP2GTSingleObjectFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTP2GTSingleObjectFilter',
    saveTags = cms.bool(True),
    l1GTAlgoBlockTag = cms.InputTag('l1tGTAlgoBlockProducer'),
    minN = cms.uint32(1),
    l1GTAlgos = cms.VPSet(
      template = cms.PSetTemplate(
        name = cms.string(''),
        collection = cms.PSet(
          objectType = cms.string('CL2Taus'),
          minPt = cms.double(0),
          maxAbsEta = cms.double(1000000000)
        )
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
