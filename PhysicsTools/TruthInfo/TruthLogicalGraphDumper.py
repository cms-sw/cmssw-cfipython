import FWCore.ParameterSet.Config as cms

def TruthLogicalGraphDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('TruthLogicalGraphDumper',
    src = cms.InputTag('truthLogicalGraphProducer'),
    rawSrc = cms.InputTag('truthGraphProducer'),
    hitIndex = cms.InputTag(''),
    hgcalRecHits = cms.VInputTag(
      'HGCalRecHit:HGCEERecHits',
      'HGCalRecHit:HGCHEFRecHits',
      'HGCalRecHit:HGCHEBRecHits'
    ),
    pfRecHits = cms.VInputTag(
      'particleFlowRecHitECAL',
      'particleFlowRecHitHBHE',
      'particleFlowRecHitHF',
      'particleFlowRecHitHO'
    ),
    dotFile = cms.string('truthlogicalgraph.dot'),
    jsonFile = cms.string(''),
    layout = cms.string('dot'),
    dumpSimHits = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
